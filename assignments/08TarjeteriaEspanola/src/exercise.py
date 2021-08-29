def main():
    return()

# vellum paper = 12 tarjetas
# pen = 35 tarjetas

vellum = int(input("Insert the vellum paper quantity: "))
pen = int(input("Insert the pen quantity: "))

vellum_qua = vellum*12
pen_qua = pen*35

if vellum_qua > pen_qua:
    print("The maximum # of cards you can print is:", pen_qua)
elif vellum_qua < pen_qua:
    print("The maximum # of cards you can print is:", vellum_qua)
