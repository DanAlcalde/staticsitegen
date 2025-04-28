from textnode import TextNode, TextType 

def main():
    test = TextNode("This is anchor text", TextType.LINK_TEXT, "https://www.boot.dev")
    print(test)

if __name__ == "__main__":
    main()