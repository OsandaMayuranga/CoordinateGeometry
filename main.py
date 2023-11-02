x = 1
while x == 1:
    begin = (int(input("\nEnter 1 to continue or 0 to exit: ")))
    if begin == 1:
        print("\nNo.1 --> length of the straight line joining two given points\n"
              "No.2 --> Internal division of a line segment joining two given points in a given ratio\n"
              "No.3 --> Mid point of the joining two points\n"
              "No.4 --> External division of a line segment joining two given points in a given ratio\n"
              "No.5 --> Coordinotes of the centroid\n"
              "No.6 --> Area of a triangle\n")

        No = int(input("Input The Number: "))

        if No == 1:
            #length of the straight line joining two given points
            print("length of the straight line joining two given points\n\nInput first point: ")
            first_x1 = int(input("x1: "))
            first_y1 = int(input("y1: "))
            print("Input second point: ")
            first_x2 = int(input("x2: "))
            first_y2 = int(input("y2: "))

            first_step_01 = ((first_x1 - first_x2) ** 2) + ((first_y1 - first_y2) ** 2)
            first_step_02 = first_step_01 ** 0.5

            if int(first_step_02) == first_step_02:
                print(f"\nSquare root of {first_step_01}")
                print(f"Answer: {(int(first_step_02))}")
            else:
                print(f"\nAnswer:\nSquare root of {first_step_01}")

        elif No == 2:
            #Internal division of a line segment joining two given points in a given ratio
            print("Internal division of a line segment joining two given points in a given ratio\n\nInput first point: ")
            second_x1 = int(input("x1: "))
            second_y1 = int(input("y1: "))
            print("Input second point: ")
            second_x2 = int(input("x2: "))
            second_y2 = int(input("y2: "))
            second_m = int(input("\nInput m: "))
            second_n = int(input("Input n: "))

            second_step_01 = ((second_m * second_x2) + (second_n * second_x1) )
            second_step_02 = ((second_m * second_y2) + (second_n * second_y1) )
            second_step_03 = (second_m + second_n)
            second_step_04 = second_step_01 / second_step_03
            second_step_05 = second_step_02 / second_step_03

            if second_step_01 % second_step_03 == 0 and second_step_02 % second_step_03 == 0:
                print(f"\nAnswer:\n({int(second_step_04)}, {int(second_step_05)})")
            elif second_step_01 % second_step_03 == 0:
                print(f"\nAnswer:\n({int(second_step_04)}, {second_step_02}/{second_step_03})")
            elif second_step_02 % second_step_03 == 0:
                print(f"\nAnswer:\n({second_step_01}/{second_step_03}, {int(second_step_05)})")
            else:
                print(f"\nAnswer:\n({second_step_01}/{second_step_03}, {second_step_02}/{second_step_03})")

        elif No == 3:
            #Mid point of the joining two points
            print("Mid point of the joining two points\n\nInput first point: ")
            third_x1 = int(input("x1: "))
            third_y1 = int(input("y1: "))
            print("Input second point: ")
            third_x2 = int(input("x2: "))
            third_y2 = int(input("y2: "))

            third_step_01 = (third_x1 + third_x2)
            third_step_02 = (third_y1 + third_y2)
            third_step_03 = third_step_01 / 2
            third_step_04 = third_step_02 / 2

            if third_step_01 % 2 == 0 and third_step_02 % 2 == 0:
                print(f"\nAnswer:\n({int(third_step_03)}, {int(third_step_04)})")
            elif third_step_01 % 2 == 0:
                print(f"\nAnswer:\n({int(third_step_03)}, {third_step_02}/2)")
            elif third_step_02 % 2 == 0:
                print(f"\nAnswer:\n({third_step_01}/2, {int(third_step_04)})")
            else:
                print(f"\nAnswer:\n({third_step_01}/2, {third_step_02}/2)")

        elif No == 4:
            #External division of a line segment joining two given points in a given ratio
            print("External division of a line segment joining two given points in a given ratio\n\nInput first point: ")
            fourth_x1 = int(input("x1: "))
            fourth_y1 = int(input("y1: "))
            print("Input second point: ")
            fourth_x2 = int(input("x2: "))
            fourth_y2 = int(input("y2: "))
            fourth_m = int(input("\nInput m: "))
            fourth_n = int(input("Input n: "))

            fourth_step_01 = ((fourth_m * fourth_x2) - (fourth_n * fourth_x1))
            fourth_step_02 = ((fourth_m * fourth_y2) - (fourth_n * fourth_y1))
            fourth_step_03 = (fourth_m - fourth_n)
            fourth_step_04 = fourth_step_01 / fourth_step_03
            fourth_step_05 = fourth_step_02 / fourth_step_03

            if fourth_step_01 % fourth_step_03 == 0 and fourth_step_02 % fourth_step_03 == 0:
                print(f"\nAnswer:\n({int(fourth_step_04)}, {int(fourth_step_05)})")
            elif fourth_step_01 % fourth_step_03 == 0:
                print(f"\nAnswer:\n({int(fourth_step_04)}, {fourth_step_02}/{fourth_step_03})")
            elif fourth_step_02 % fourth_step_03 == 0:
                print(f"\nAnswer:\n({fourth_step_01}/{fourth_step_03}, {int(fourth_step_05)})")
            else:
                print(f"\nAnswer:\n({fourth_step_01}/{fourth_step_03}, {fourth_step_02}/{fourth_step_03})")

        elif No == 5:
            #Coordinotes of the centroid
            print("Coordinotes of the centroid\n\nInput first point: ")
            fifth_x1 = int(input("x1: "))
            fifth_y1 = int(input("y1: "))
            print("Input second point: ")
            fifth_x2 = int(input("x2: "))
            fifth_y2 = int(input("y2: "))
            print("Input third point: ")
            fifth_x3 = int(input("x3: "))
            fifth_y3 = int(input("y3: "))

            fifth_step_01 = (fifth_x1 + fifth_x2 + fifth_x3)
            fifth_step_02 = (fifth_y1 + fifth_y2 + fifth_y3)
            fifth_step_03 = fifth_step_01 / 3
            fifth_step_04 = fifth_step_02 / 3

            if fifth_step_01 % 3 == 0 and fifth_step_02 % 3 == 0:
                print(f"\nAnswer:\n({int(fifth_step_03)}, {int(fifth_step_04)})")
            elif fifth_step_01 % 3 == 0:
                print(f"\nAnswer:\n({int(fifth_step_03)}, {fifth_step_02}/3)")
            elif fifth_step_02 % 3 == 0:
                print(f"\nAnswer:\n({fifth_step_01}/3, {int(fifth_step_04)})")
            else:
                print(f"\nAnswer:\n({fifth_step_01}/3, {fifth_step_02}/3)")

        elif No == 6:
            #Area of a triangle
            print("Area of a triangle\n\nInput first point: ")
            sixth_x1 = int(input("x1: "))
            sixth_y1 = int(input("y1: "))
            print("Input second point: ")
            sixth_x2 = int(input("x2: "))
            sixth_y2 = int(input("y2: "))
            print("Input third point: ")
            sixth_x3 = int(input("x3: "))
            sixth_y3 = int(input("y3: "))

            sixth_01 = int(sixth_x1 * (sixth_y2 - (sixth_y3)))
            sixth_02 = int(sixth_x2 * (sixth_y3 - (sixth_y1)))
            sixth_03 = int(sixth_x3 * (sixth_y1 - (sixth_y2)))

            sixth_step_01 = (sixth_01) + (sixth_02) + (sixth_03)
            sixth_step_02 = sixth_step_01 * -1

            if sixth_step_01 < 0:
                sixth_step_01 = sixth_step_02
            else:
                sixth_step_01 = sixth_step_01

            sixth_step_03 = (sixth_step_01) / 2

            if sixth_step_01 % 2 == 0:
                print(f"\nAnswer:\n{(int(sixth_step_03))}")
            else:
                print(f"\nAnswer:\n{(int(sixth_step_01))}/2")

    elif begin == 0:
        exit()