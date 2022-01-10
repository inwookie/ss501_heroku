import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import segmentation_models_pytorch as smp


def app():
    @st.cache(allow_output_mutation=True, ttl=3600)
    def load_model():
        model = torch.load('better_result_light.pth',
                           map_location=torch.device('cpu'))
        model.eval()
        return model

    with st.spinner('Model is being loaded..'):
        model = load_model()

    st.write("""
            # Scratch 
            """
             )

    file = st.file_uploader(
        "Please upload a scratch image", type=["jpg", "jpeg"])
    if file is not None:
        path_in = file.name
        print(path_in)
    else:
        path_in = None
    st.set_option('deprecation.showfileUploaderEncoding', False)

    infer_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
        transforms.Resize((320, 320))
    ])

    if file is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file)

        device = 'cpu'
        input_image = infer_transform(image).to('cpu')

        output = model(input_image.unsqueeze(dim=0))

        output = torch.as_tensor((output - 0.5) > 0, dtype=torch.int32)

        out_target = torch.argmax(output.to("cpu"), dim=1).to("cpu").byte()

        target = transforms.ToPILImage()(out_target)
        # target.save('target.jpg')
        # image.save('image.jpg')
        images = np.asarray(image)
        targets = np.asarray(target)
        # print(images.shape)
        import cv2
        width, height = image.size
        #src = cv2.imread('target.jpg',cv2.IMREAD_GRAYSCALE)
        src = cv2.resize(targets, (width, height))

        _, src_bin = cv2.threshold(src, 127, 255, cv2.THRESH_OTSU)

        cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(
            src_bin)

        for i in range(1, cnt):
            (x, y, w, h, area) = stats[i]

            # 노이즈 제거
            if area < 200:
                continue
            cv2.rectangle(images, (x, y, w, h), (255, 0, 0), 3)

        image2 = Image.fromarray(images)

        st.markdown("""
        ## Scratch Detected Image
        """)
        st.image(image2, use_column_width=True)

        st.markdown("""
        ## Original Image
        """)

        st.image(Image.open(file), use_column_width=True)
