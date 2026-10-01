import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('example.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_value = 127
kernel_size = 3

while True:
    print("\n1. Original")
    print("2. Grayscale")
    print("3. Blur")
    print("4. Edge Detection")
    print("5. Threshold")
    print("6. Change Threshold")
    print("7. Change Kernel Size")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(result)
        plt.title("Original Image")
        plt.axis("off")
        plt.show()

    elif choice == "2":
        plt.imshow(gray, cmap="gray")
        plt.title("Grayscale")
        plt.axis("off")
        plt.show()

    elif choice == "3":
        result = cv2.GaussianBlur(
            image, (kernel_size, kernel_size), 0
        )
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        plt.imshow(result)
        plt.title("Blurred Image")
        plt.axis("off")
        plt.show()

    elif choice == "4":
        edges = cv2.Canny(gray, 100, 200)
        plt.imshow(edges, cmap="gray")
        plt.title("Edge Detection")
        plt.axis("off")
        plt.show()

    elif choice == "5":
        _, result = cv2.threshold(
            gray, threshold_value, 255, cv2.THRESH_BINARY
        )
        plt.imshow(result, cmap="gray")
        plt.title("Threshold")
        plt.axis("off")
        plt.show()

    elif choice == "6":
        threshold_value = int(input("Enter threshold (0-255): "))

    elif choice == "7":
        kernel_size = int(input("Enter kernel size (3, 5, 7...): "))

        if kernel_size % 2 == 0:
            kernel_size += 1

    elif choice == "8":
        break

    else:
        print("Invalid choice!")