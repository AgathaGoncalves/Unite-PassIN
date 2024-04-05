class Test:
    def __enter__(self):
        print('teste aaaaaaaaaaaaaaaaa')
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('ceeeeeeeeeeeeeeeeeeeeeee')
        

with Test() as ola:
    print('beeeeeeeeeeeeeee')
