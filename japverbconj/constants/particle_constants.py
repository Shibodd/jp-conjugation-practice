A_PARTICLE = "あ"
E_PARTICLE = "え"
I_PARTICLE = "い"
O_PARTICLE = "お"
U_PARTICLE = "う"

KA_PARTICLE = "か"
KE_PARTICLE = "け"
KI_PARTICLE = "き"
KO_PARTICLE = "こ"
KU_PARTICLE = "く"

GA_PARTICLE = "が"
GE_PARTICLE = "げ"
GI_PARTICLE = "ぎ"
GO_PARTICLE = "ご"
GU_PARTICLE = "ぐ"

SA_PARTICLE = "さ"
SE_PARTICLE = "せ"
SHI_PARTICLE = "し"
SO_PARTICLE = "そ"
SU_PARTICLE = "す"

TA_PARTICLE = "た"
TE_PARTICLE = "て"
CHI_PARTICLE = "ち"
TO_PARTICLE = "と"
TSU_PARTICLE = "つ"

DA_PARTICLE = "だ"
DE_PARTICLE = "で"
DI_PARTICLE = "ぢ"
DO_PARTICLE = "ど"
DU_PARTICLE = "づ"

NA_PARTICLE = "な"
NE_PARTICLE = "ね"
NI_PARTICLE = "に"
NO_PARTICLE = "の"
NU_PARTICLE = "ぬ"

HA_PARTICLE = "は"
HE_PARTICLE = "へ"
HI_PARTICLE = "ひ"
HO_PARTICLE = "ほ"
HU_PARTICLE = "ふ"

BA_PARTICLE = "ば"
BE_PARTICLE = "べ"
BI_PARTICLE = "び"
BO_PARTICLE = "ぼ"
BU_PARTICLE = "ぶ"

PA_PARTICLE = "ぱ"
PE_PARTICLE = "ぺ"
PI_PARTICLE = "ぴ"
PO_PARTICLE = "ぽ"
PU_PARTICLE = "ぷ"

MA_PARTICLE = "ま"
ME_PARTICLE = "め"
MI_PARTICLE = "み"
MO_PARTICLE = "も"
MU_PARTICLE = "む"

YA_PARTICLE = "や"
YU_PARTICLE = "ゆ"
YO_PARTICLE = "よ"

RA_PARTICLE = "ら"
RE_PARTICLE = "れ"
RI_PARTICLE = "り"
RO_PARTICLE = "ろ"
RU_PARTICLE = "る"

WA_PARTICLE = "わ"
WO_PARTICLE = "を"
N_PARTICLE = "ん"

CHISAI_TSU_PARTICLE = "っ"

ENDING_DICT = {
    U_PARTICLE: {
        A_PARTICLE: WA_PARTICLE,
        I_PARTICLE: I_PARTICLE,
        U_PARTICLE: U_PARTICLE,
        E_PARTICLE: E_PARTICLE,
        O_PARTICLE: O_PARTICLE,
    },
    KU_PARTICLE: {
        A_PARTICLE: KA_PARTICLE,
        I_PARTICLE: KI_PARTICLE,
        U_PARTICLE: KU_PARTICLE,
        E_PARTICLE: KE_PARTICLE,
        O_PARTICLE: KO_PARTICLE,
    },
    GU_PARTICLE: {
        A_PARTICLE: GA_PARTICLE,
        I_PARTICLE: GI_PARTICLE,
        U_PARTICLE: GU_PARTICLE,
        E_PARTICLE: GE_PARTICLE,
        O_PARTICLE: GO_PARTICLE,
    },
    SU_PARTICLE: {
        A_PARTICLE: SA_PARTICLE,
        I_PARTICLE: SHI_PARTICLE,
        U_PARTICLE: SU_PARTICLE,
        E_PARTICLE: SE_PARTICLE,
        O_PARTICLE: SO_PARTICLE,
    },
    TSU_PARTICLE: {
        A_PARTICLE: TA_PARTICLE,
        I_PARTICLE: CHI_PARTICLE,
        U_PARTICLE: TSU_PARTICLE,
        E_PARTICLE: TE_PARTICLE,
        O_PARTICLE: TO_PARTICLE,
    },
    NU_PARTICLE: {
        A_PARTICLE: NA_PARTICLE,
        I_PARTICLE: NI_PARTICLE,
        U_PARTICLE: NU_PARTICLE,
        E_PARTICLE: NE_PARTICLE,
        O_PARTICLE: NO_PARTICLE,
    },
    BU_PARTICLE: {
        A_PARTICLE: BA_PARTICLE,
        I_PARTICLE: BI_PARTICLE,
        U_PARTICLE: BU_PARTICLE,
        E_PARTICLE: BE_PARTICLE,
        O_PARTICLE: BO_PARTICLE,
    },
    MU_PARTICLE: {
        A_PARTICLE: MA_PARTICLE,
        I_PARTICLE: MI_PARTICLE,
        U_PARTICLE: MU_PARTICLE,
        E_PARTICLE: ME_PARTICLE,
        O_PARTICLE: MO_PARTICLE,
    },
    RU_PARTICLE: {
        A_PARTICLE: RA_PARTICLE,
        I_PARTICLE: RI_PARTICLE,
        U_PARTICLE: RU_PARTICLE,
        E_PARTICLE: RE_PARTICLE,
        O_PARTICLE: RO_PARTICLE,
    },
}