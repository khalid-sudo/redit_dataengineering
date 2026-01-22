import os
def main():
    print(f"os.path.dirname(os.path.dirname(os.path.abspath(__file__))) -> {os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}")
    print(f"os.path.dirname(os.path.abspath(__file__)) -> {os.path.dirname(os.path.abspath(__file__))}")
    print(f"os.path.abspath(__file__) -> ", os.path.abspath(__file__))


if __name__ == "__main__":
    main()
