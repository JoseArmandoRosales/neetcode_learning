class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Si las longitudes son distintas, no puede ser anagrama
        if len(s) != len(t):
            return False

        # Diccionarios para contar letras de cada cadena
        s_hashmap, t_hashmap = {}, {}

        # Recorremos ambas cadenas AL MISMO TIEMPO en un solo loop
        for char_s, char_t in zip(s, t):
            s_hashmap[char_s] = s_hashmap.get(char_s, 0) + 1
            t_hashmap[char_t] = t_hashmap.get(char_t, 0) + 1

        # Comparamos ambos diccionarios directamente
        return s_hashmap == t_hashmap