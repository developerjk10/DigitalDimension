def headerFooter_dec(func):
    def wrapperfunc (func):
        #Before Function
        print("Header")
        func()
        #After Function
        print("Footer")

@headerFooter_dec
def letter():
    print("Example Letter")

letter()
