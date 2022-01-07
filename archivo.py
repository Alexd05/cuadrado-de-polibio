print("\nescriba c (cifrar) o d (decifrar) no agregue más texto, recuerde no usar ñ, más información https://museo.inf.upv.es/blog/2021/05/14/cifrado-de-polibio/")

accion = input("\ndesea cifrar o decifrar? ")

if "c" in accion:

  print('\nPara cifrar ingrese en minusculas y sin acentos, tenga en cuenta que se usa el "Cuadrado de Polibio"')

  textoc  = input("\nIngrese el texto a cifrar ")

  resc = textoc.replace("a", "11").replace("b", "12").replace("c", "13").replace("d", "14").replace("e", "15").replace("f", "21").replace("g", "22").replace("h", "23").replace("i", "24").replace("j", "24").replace("k", "25").replace("l", "31").replace("m", "32").replace("n", "33").replace("o", "34").replace("p", "35").replace("q", "41").replace("r", "42").replace("s", "43").replace("t", "44").replace("u", "45").replace("v", "51").replace("w", "52").replace("x", "53").replace("y", "54").replace("z", "55").replace(" ", "")

  print(f"\nEl texto cifrado es: {resc}\n")

elif "C" in accion:

  print('\nPara cifrar ingrese en minusculas y sin acentos, tenga en cuenta que se usa el "Cuadrado de Polibio"')

  textoc  = input("\ningrese su texto a cifrar ")

  resc = textoc.replace("a", "11").replace("b", "12").replace("c", "13").replace("d", "14").replace("e", "15").replace("f", "21").replace("g", "22").replace("h", "23").replace("i", "24").replace("j", "24").replace("k", "25").replace("l", "31").replace("m", "32").replace("n", "33").replace("o", "34").replace("p", "35").replace("q", "41").replace("r", "42").replace("s", "43").replace("t", "44").replace("u", "45").replace("v", "51").replace("w", "52").replace("x", "53").replace("y", "54").replace("z", "55").replace(" ", "")

  print(f"\nEl texto cifrado es: {resc}\n")

elif "d" in accion:
    print('\nPara decifrar solo ingrese números, recuerde que se usa el "Cuadrado de Polibio", para más información https://museo.inf.upv.es/blog/2021/05/14/cifrado-de-polibio/')
    
    textod = input("Ingrese los números a decifrar ")

    resd = textod.replace("11", "a").replace("12", "b").replace("13", "c").replace("14", "d").replace("15", "e").replace("21", "f").replace("22", "g").replace("23", "h").replace("24", "i").replace("24", "j").replace("25", "k").replace("31", "l").replace("32", "m").replace("33", "n").replace("34", "o").replace("35", "p").replace("41", "q").replace("42", "r").replace("43", "s").replace("44", "t").replace("45", "u").replace("51", "v").replace("52", "w").replace("53", "x").replace("54", "y").replace("55", "z").replace("", " ")

    print(f"\nEl texto decifrado es: {resd}\n")

elif "D" in accion:
    print('\nPara decifrar solo ingrese números sin espacios, recuerde que se usa el "Cuadrado de Polibio", para más información https://museo.inf.upv.es/blog/2021/05/14/cifrado-de-polibio/')
    
    textod = input("Ingrese los números a decifrar ")

    resd = textod.replace("11", "a").replace("12", "b").replace("13", "c").replace("14", "d").replace("15", "e").replace("21", "f").replace("22", "g").replace("23", "h").replace("24", "i").replace("24", "j").replace("25", "k").replace("31", "l").replace("32", "m").replace("33", "n").replace("34", "o").replace("35", "p").replace("41", "q").replace("42", "r").replace("43", "s").replace("44", "t").replace("45", "u").replace("51", "v").replace("52", "w").replace("53", "x").replace("54", "y").replace("55", "z").replace("", " ")

    print(f"\nEl texto decifrado es: {resd}\n")
