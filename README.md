# NCP CFR Python Module

## 1. Usage

1. get_celeb_similarity
    - 사진하나의 path 를 Path 객체로 넘기면, 해당 사진에 대한 유명인사와 유사성 정보를 볼 수 있다.
2. get_bulk_celeb_similarity
    - 사진들이 담겨있는 directory path 를 Path 객체로 넘기면 bulk 로 처리한다.
3. get_face_sensing_info
    - 사진하나의 path 를 Path 객체로 넘기면, 해당 사진에 대한 분석 정보를 볼 수 있다.
4. get_bulk_face_sensing_info
    - 사진들이 담겨있는 directory path 를 Path 객체로 넘기면 bulk 로 처리한다.

Example :
```
from NCP_CFR.CFR import CFR

cfr = CFR(client_id="YOUR CLIENT ID", client_secret="YOUR CLIENT SECRET")

result1 = cfr.get_celeb_similarity(Path("/Users/naver/Desktop/sample.jpg"))
result2 = cfr.get_face_sensing_info(Path("/Users/naver/Desktop/sample.jpg"))
print(result1)
print(result2)

result3 = cfr.get_bulk_celeb_similarity(Path("/Users/naver/Desktop/sample"))
result4 = cfr.get_bulk_celeb_similarity(Path("/Users/naver/Desktop/sample"))
print(result3)
print(result4)
```
