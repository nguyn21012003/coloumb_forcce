from math import sqrt


class number_e:
    def __init__(self, n, x, y, q) -> None:
        self.n = n
        self.x = x
        self.y = y
        self.q = q


def array_handle_e_value(n: int):
    n = int(n)
    array_e = []

    for i in range(n):
        x, y, q = input("nhập vào tọa độ x,y và điện tích: ").split(",")
        e = number_e(n, x, y, q)
        e_x = e.x
        e_y = e.y
        e_q = e.q
        coor = {}
        coor["e tại vị trí"] = i
        coor["x"] = e_x
        coor["y"] = e_y
        coor["q"] = e_q
        array_e.append(coor)

    # print(coor)

    return array_e


def coulomb_force(array):
    f = []
    for i in range(len(array)):
        k = 9e9
        sigma_f = 0
        x_0, y_0, q_0 = float(array[1]["x"]), float(array[0]["y"]), float(array[0]["q"])
        for j in range(len(array)):
            if i != j:
                x_j, y_j, q_j = float(array[j]["x"]), float(array[j]["y"]), float(array[j]["q"])
                r = abs(sqrt((x_j - x_0) ** 2 + (y_j - y_0) ** 2))
                f_ij = (k * q_0 * q_j) / r**2
                sigma_f += f_ij
        f.append(sigma_f)

    return f


def main():
    print(coulomb_force(array_handle_e_value(input("Nhập vào số điện tích điểm: "))))
    # print(array_handle_e_value(input("Nhập vào số điện tích điểm: ")))


if __name__ == "__main__":
    main()
