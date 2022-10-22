def demo(anum):
    if anum > 0:
        print(f'id: {id(anum)} num: {anum}')
        demo(anum -1)


demo(6)