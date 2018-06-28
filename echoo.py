def echo(*args,**kwargs):
    print(args,kwargs)
    type(args)
echo("a","b",a=3,b=4)