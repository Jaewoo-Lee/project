import base64
import cv2


class ModImg:
    #     생성자
    def __init__(self, img, size, times):
        #         원본 이미지
        self.img = img
        #         input 사이즈
        self.size = size
        #         이미지 크기를 확장할 배수 (ex) 2배, 4배, 8배 ...)
        self.times = times

        #         padding 크기
        self.padh = 0
        self.padw = 0

        h, w, _ = img.shape
        
        if h % 2 == 1:
                self.img = self.img[:h-1, :]
                h -= 1
        if w % 2 == 1:
                self.img = self.img[: , :w-1]
                w -= 1
        #         이미지가 input 사이즈보다 작으면 padding
        #         이미지가 input 사이즈보다 크면 이미지를 자른다
        if h < self.size:
            self.padh = int((self.size - h) / 2)
        else:
            hh = int((h - self.size) / 2)
            self.img = self.img[hh:(h - hh), :]

        if w < self.size:
            self.padw = int((self.size - w) / 2)
        else:
            ww = int((w - self.size) / 2)
            self.img = self.img[ : ,ww:(w - ww)]

    #     원본 이미지
    def getImg(self):
        return self.img

    #     Padding 이미지
    def getPadImg(self):
        return cv2.copyMakeBorder(self.img, top=self.padh, bottom=self.padh, left=self.padw, right=self.padw,
                                  borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0))

    #     모델을 통해 예측된 이미지의 padding 제거
    def cutPadImg(self, pred):
        h, w, _ = pred.shape
        return pred[int(self.padh * self.times):int(h - self.padh * self.times),
               int(self.padw * self.times):int(w - self.padw * self.times)]

    #     이미지를 다운로드 가능한 링크로 변환
    def getURI(self, image, contentType):
        #         OpenCv는 BGR을 사용하기에 RGB로 변경한다
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        converted = cv2.imencode('.jpg', imageRGB)[1].tostring()
        uri = ("data:" + contentType + ";" + "base64," + base64.b64encode(converted).decode('utf-8'))
        return uri


    #     테스트를 위하여 이미지 크기를 2배씩 늘림
    def getTimes(self, img):
        return cv2.pyrUp(img)
