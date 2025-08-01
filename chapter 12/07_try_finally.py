def main():

    try:
        a = int(input("heyy, Enter a number: "))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("Hey I am inside of finally")  # Executed regardless of error!

main()   