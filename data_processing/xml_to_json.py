import json
import xmltodict

with open("../data/xml_to_json.xml", "r") as f:
    xml_data = f.read()

print(f"\nxml 데이터 파일 읽어와서 출력한 결과: \n{xml_data}")

json_data = json.dumps(xmltodict.parse(xml_data), indent=4)

print(f"\njson 데이터로 변환하여 출력한 결과: \n{json_data}")