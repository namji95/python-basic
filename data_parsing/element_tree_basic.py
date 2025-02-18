import os
import xml.dom.minidom
import xml.etree.ElementTree as ET


class ElementTreeBasic:
    def element_tree_basic(self):
        print("Element Tree Basic")

        save_path = r"C:\WorkSpace\python-basic\data\element_tree_basic_data.xml"

        # 기존 XML 파일이 존재하면 삭제
        if os.path.exists(save_path):
            os.remove(save_path)
            print(f"기존 XML 파일 삭제: {save_path}")

        print("\n-----Element Tree 생성 및 저장-----")
        # 루트 요소 생성
        library = ET.Element("library")  # <library> 태그 생성
        # 책 데이터 추가
        self.add_book(library, "101", "Python Programming", "John Doe", "Programming", 2021, True)
        self.add_book(library, "102", "Machine Learning Basics", "Jane Smith", "AI", 2020, False)
        self.add_book(library, "103", "Data Science Handbook", "Emily White", "Data Science", 2019, True)

        # 저장할 폴더 설정 (C:\WorkSpace\python-basic\data\library.xml)
        save_path = os.path.join("C:\WorkSpace\python-basic\data", "element_tree_basic_data.xml")

        # 폴더가 없으면 생성
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # XML 파일 저장
        tree = ET.ElementTree(library)
        tree.write(save_path, encoding="utf-8", xml_declaration=True)

        print(f"XML 파일이 저장된 위치: {os.path.abspath(save_path)}")

        print("\n-----xml 파일 읽기 및 모든 책 정보 출력-----")
        # 파일 경로 지정
        file_path = r"C:\WorkSpace\python-basic\data\element_tree_basic_data.xml"  # raw string 사용

        # XML 파일 파싱
        tree = ET.parse(file_path)  # 파일을 파싱하여 트리 객체 생성
        root = tree.getroot()  # 루트 요소 가져오기

        # 모든 책 정보 출력
        for book in root.findall("book"):
            book_info = self.print_element(book)

            print(book_info)

        print("\n-----xml 특정 조건의 책 찾기 (AI 장르 책 검색)-----")
        for book in root.findall("book"):
            if book.find("genre").text == "AI":
                print(f"AI 관련 도서: {book.find('title').text} by {book.find('author').text}")

        print("\n-----xml 정보 수정 (출판 연도 업데이트)-----")
        print("수정 전")
        for book in root.findall("book"):
            book_info = self.print_element(book)
            print(book_info)

        for book in root.findall("book"):
            if book.get("id") == "103":
                book.find("published").text = "1995"

        print("\n수정 후")
        for book in root.findall("book"):
            book_info = self.print_element(book)
            print(book_info)

        print("\n-----xml 정보 추가 (새로운 책 추가)-----")
        file_path = r"C:\WorkSpace\python-basic\data\element_tree_basic_data.xml"

        tree = ET.parse(file_path)
        root = tree.getroot()

        new_book = ET.SubElement(root, "book", id="104")
        ET.SubElement(new_book, "title").text = "Deep Learning Guide"
        ET.SubElement(new_book, "author").text = "Michael Brown"
        ET.SubElement(new_book, "genre").text = "AI"
        ET.SubElement(new_book, "published").text = "2023"
        ET.SubElement(new_book, "available").text = "true"

        tree.write(file_path, encoding="utf-8", xml_declaration=True)

        root = tree.getroot()
        for book in root.findall("book"):
            book_info = self.print_element(book)
            print(book_info)

        print("\n-----xml 정보 삭제 (대출 불가능한 책 제거)-----")
        for book in root.findall("book"):
            if book.find("available").text == "false":
                root.remove(book)

        tree.write(file_path, encoding="utf-8", xml_declaration=True)

        for book in root.findall("book"):
            book_info = self.print_element(book)
            print(book_info)

        print("\n-----XPath를 활용하여 xml 특정 요소 찾기-----")
        book = root.find(".//book[@id='101']")
        if book is not None:
            print(f"ID 101 도서 제목: {book.find('title').text}")

        print("\n-----XML Pretty Print (XML 데이터 가독성 좋게 출력)-----")
        xml_str = ET.tostring(root, encoding="utf-8")
        pretty_xml = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="  ")
        print(pretty_xml)

    def add_book(self, library, book_id, title, author, genre, published, available):
        # 책을 추가하는 함수 정의
        book = ET.SubElement(library, "book", id=book_id) # <book> 태그 생성 (id 속성 추가)
        ET.SubElement(book, "title").text = title # <title> 태그 생성 및 텍스트 추가
        ET.SubElement(book, "author").text = author # <author> 태그 생성 및 텍스트 추가
        ET.SubElement(book, "genre").text = genre # <genre> 태그 생성 및 텍스트 추가
        ET.SubElement(book, "published").text = str(published) # <published> 태그 생성 및 텍스트 추가
        ET.SubElement(book, "available").text = str(available).lower() # <available> 태그 생성 및 (소문자로 변환)

    def print_element(self, book):
        book_id = book.get("id")
        title = book.find("title").text
        author = book.find("author").text
        genre = book.find("genre").text
        published = book.find("published").text
        available = book.find("available").text

        book_info = (f"id: {book_id}, "
                     f"title: {title}, "
                     f"author: {author}, "
                     f"genre: {genre}, "
                     f"published: {published}, "
                     f"available: {available}")

        return book_info

if __name__ == '__main__':
    element_tree_basic = ElementTreeBasic()
    element_tree_basic.element_tree_basic()