def average(array):
    plant_height = set(array)

    return sum(plant_height) / len(plant_height)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
