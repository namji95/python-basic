import xml.etree.cElementTree as ET


class ElementTreeTestCode:
    def __init__(self, file_path):
        self.file_path = file_path

    def string_et_test(self):
        xml = """<?xml version = "1.0" encoding = "UTF-8" ?> 
        <root> 
            <sub rank="1" id="apple" price="120" u="up">애플
                <desc name="ipod">아이팟</desc>
                <desc name="phone">아이폰</desc>       
            </sub>
            <sub rank="2" id="tsla" price="820" u="up">테슬라</sub>
            <sub rank="3" id="msft" price="233" u="down">마소</sub>
        </root>
        """

        r = ET.fromstring(xml)
        print("=========root 하위 find사용 직접 꺼내기=========")
        print(r.find('sub').get('rank'))
        print(r.find('sub')[0].get('name'))
        print(r.find('sub')[1].text)
        print(r[0].text)

        print("=========root 하위 get 직접꺼내기=========")
        print(r[1].get("rank"))
        print(r[1].get("id"))
        print(r[1].get("price"))
        print(r[1].text)

        print("\n=========root 하위 get 반복문=========")
        for tag in r:
            print(tag.get("rank"))
            print(tag.get("id"))
            print(tag.get("price"))
            print(tag.text)
            if len(tag) > 0:
                print(",".join(v.get("name") for v in tag))

    def file_et_test(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        print("\n")
        print(root.tag)

        # for child in root:
        #     print(child.tag, child.attrib)

if __name__ == '__main__':
    et_test = ElementTreeTestCode("C:\workSpace\pythonBasic\data\elementTreeData.xml")
    et_test.string_et_test()
    et_test.file_et_test()