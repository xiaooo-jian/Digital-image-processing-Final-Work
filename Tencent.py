# pip install tencentcloud-sdk-python
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
import base64
import cv2
import json
import jsonpath


def text_recognition(image):
    image = cv2.imencode('.jpg', image)[1]

    image_code = str(base64.b64encode(image))[2:-1]
    text = str(get_text(image_code))
    text = json.loads(text)
    DetectedText = jsonpath.jsonpath(text, "$..DetectedText")
    return DetectedText


def get_text(image_code):
    try:
        cred = credential.Credential("AKIDVmoHVSqfttfBRXRajeIq8Axf15udmSYP", "ymLfjY7TZkjY9XgdHg6MM9gyY3Qnzvyl")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-guangzhou", clientProfile)

        req = models.GeneralBasicOCRRequest()
        params = '{"ImageBase64":"' + image_code + '"}'
        req.from_json_string(params)

        resp = client.GeneralBasicOCR(req)
        return resp.to_json_string()
    except TencentCloudSDKException as err:
        print(err)
