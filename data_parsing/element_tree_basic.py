import os
import xml.etree.ElementTree as ET


class ElementTreeBasic:
    def element_tree_basic(self):
        print("Element Tree Basic")

        print("-----Element Tree 생성 및 저장-----")
        # 루트 요소 생성
        library = ET.Element("library")  # <library> 태그 생성
        # 책 데이터 추가
        self.add_book(library, "101", "Python Programming", "John Doe", "Programming", 2021, True)
        self.add_book(library, "102", "Machine Learning Basics", "Jane Smith", "AI", 2020, False)
        self.add_book(library, "103", "Data Science Handbook", "Emily White", "Data Science", 2019, True)

        # 저장할 폴더 설정 (C:\WorkSpace\python-basic\data\library.xml)
        save_path = os.path.join("C:\WorkSpace\python-basic\data", "library.xml")

        # 폴더가 없으면 생성
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # XML 파일 저장
        tree = ET.ElementTree(library)
        tree.write(save_path, encoding="utf-8", xml_declaration=True)

        print(f"XML 파일이 저장된 위치: {os.path.abspath(save_path)}")

        print("-----xml 파일 읽기 및 모든 책 정보 출력-----")
        # 파일 경로 지정
        file_path = r"C:\WorkSpace\python-basic\data\element_tree_basic_data.xml"  # raw string 사용

        # XML 파일 파싱
        tree = ET.parse(file_path)  # 파일을 파싱하여 트리 객체 생성
        root = tree.getroot()  # 루트 요소 가져오기

        # 모든 책 정보 출력
        for book in root.findall("book"):
            book_id = book.get("id")
            title = book.find("title").text
            author = book.find("author").text
            genre = book.find("genre").text
            published = book.find("published").text
            available = book.find("available").text
            print(f"[ID: {book_id}] {title} by {author} ({genre}, {published}) - Available: {available}")

    def add_book(self, library, book_id, title, author, genre, published, available):
        # 책을 추가하는 함수 정의
        book = ET.SubElement(library, "book", id=book_id) # <book> 태그 생성 (id 속성 추가)
        ET.SubElement(book, "title").text = title # <title> 태그 생성 및 텍스트 추가
        ET.SubElement(book, "author").text = author # <author> 태그 생성 및 텍스트 추가
        ET.SubElement(book, "genre").text = genre # <genre> 태그 생성 및 텍스트 추가
        ET.SubElement(book, "published").text = str(published) # <published> 태그 생성 및 텍스트 추가
        ET.SubElement(book, "available").text = str(available).lower() # <available> 태그 생성 및 (소문자로 변환)

if __name__ == '__main__':
    element_tree_basic = ElementTreeBasic()
    element_tree_basic.element_tree_basic()