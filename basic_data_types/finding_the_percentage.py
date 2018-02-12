if __name__ == '__main__':
    n = int(input())
    student_marks , arr = {},{}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    arr = student_marks[query_name]
    result = (arr[1]+arr[2]+arr[0])/3
    print("{:.2f}".format(result))
