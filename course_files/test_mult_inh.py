class A:
    def do_some(self):
        print("method from A")


class B(A):
    def do_some(self):
        print("method from B")
        super().do_some()


class C(A):
    def do_some(self):
        print("method from C")


class D(B, C):
    def do_some(self):
        print("method from D")
        super().do_some()


thing = D()
thing.do_some()
