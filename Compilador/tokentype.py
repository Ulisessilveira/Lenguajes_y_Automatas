# definir todos los tokens enumerados
import enum
class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    ##KEYWORDS
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111

    do = 112
    re = 113
    mi = 114
    fa = 115
    sol = 116
    la = 117
    si = 118
    silencio = 119
    
    NATURAL = 120
    BEMOL = 121
    SOSTENIDO = 122

    TEMPO = 123

    CANCION = 125
    PARTITURA = 126
    COMPOSICION = 127
    MUSICA = 128
    TEXTO = 129
    PIEZA = 130
    OBRA= 131

    CLAVESOL = 132
    CLAVEFA = 133
    CLAVEDO = 134

    REDONDA = 135
    BLANCA = 136
    NEGRA = 137
    CORCHEA = 138
    SEMICORCHEA =139
    FUSA = 140

    DOSCUARTOS = 141
    TRESCUARTOS = 142
    CUATROCUARTOS = 143
    SEISOCTAVOS = 144

    DOMAYOR = 145
    DOBEMOLMAYOR = 146
    SOLBEMOLMAYOR = 147
    REBEMOLMAYOR = 148
    LABEMOLMAYOR = 149
    MIBEMOLMAYOR = 150
    SIBEMOLMAYOR = 151
    FAMAYOR = 152
    SOLMAYOR = 153
    REMAYOR = 154
    LAMAYOR = 155
    MIMAYOR = 156
    SIMAYOR = 157
    FASOSTENIDOMAYOR = 158
    DOSOSTENIDOMAYOR = 159

    DECLARA = 160
    INSERTAR = 161
    ELIMINAR = 162
    MODIFICAR = 163
    EJECUTAR = 164

    ACENTO = 165
    ACENTOFUERTE = 166
    FERMATA = 167
    LIGADURA = 168
    STACCATO = 169

    ESTA = 170
    EL = 171
    LA = 172
    UN = 173
    UNA = 174
    TODO = 175
    TODOS = 176
    COMO = 177
    LOS = 178
    LAS = 179


    EN = 180
    CON = 181
    PARA = 182

    HACER = 183
    CONVERTIR = 184

    CRESCENDO = 185
    DECRESCENDO = 186
    PPP = 187
    PP = 188
    P = 189
    MP = 190
    MF = 191
    F = 192
    FF = 193
    FFF = 194

    SOBREGRAVE = 195
    GRAVE = 196
    AGUDO = 197
    SOBREAGUDO = 198

    ARMADURA = 199


    #OPERADORES
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
