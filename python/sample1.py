from memory_profiler import profile

@profile
def main():
     m = 12;
     d = 6;
     if d/m == 0:
        print('yes')
     else:
         print('no')


if __name__ == "__main__":
    main()
