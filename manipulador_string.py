class ManipuladorStrings:
    def inverter(self, texto):
        return texto[::-1]

    def contar_vogais(self, texto):
        vogais = "aeiouAEIOU"
        return sum(1 for char in texto if char in vogais)