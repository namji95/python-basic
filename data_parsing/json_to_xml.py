import json
import xmltodict

with open("../data/json_to_xml.json") as json_file:
    json_data = json_file.read()

print(f"\njson 데이터 파일 읽어와서 출력한 결과: \n{json_data}")

json_dict = json.loads(json_data)

xml_data = xmltodict.unparse({"root": json_dict}, pretty=True)

# xml의 엘리먼트 구조가 최상위 레벨의 엘리먼트가 하나라면 아래와 같이 사용할 수 있습니다.
# xml_data = xmltodict.unparse(json.loads(json_data), pretty=True)

print(f"\nxml 데이터로 변환하여 출력한 결과: \n{xml_data}")