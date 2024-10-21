def main():
    nums = {1:91, 
              2:87, 
              3:11, 
              4:80, 
              5:100}
    max_obj = max(nums.values())
    max_keys = [key for key,value in nums.items() if value == max_obj]
    print(max_keys[0], max_obj)


if __name__ == "__main__":
    main()