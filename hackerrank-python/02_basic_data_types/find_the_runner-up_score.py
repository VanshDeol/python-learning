if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max1=max(arr)
    runner_up=[x for x in arr if x < max1]
  
    print(max(runner_up))

