class Matrix:
    def __init__(self,data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    
    def __repr__(self):
        return "\n".join(["\t".join(map(str,row)) for row in self.data])
    

    
    

    

def main():
    print("Enter the first matrix: ")
    my_matrix = Matrix()
    matrix1 = my_matrix.get_matrix()


if __name__ == "__main__":
    main()