Polimorfizm nedir?
Polimorfizm - defolt gələn, inheritance aldığı classdan olan metodu dəyişmək. Mövcud könfiqrasiyanı dəyişmək.

Inheritance nedir?
İnheritance -  varislik, sahib olduğu classın metod və atributlarına çatmaq

Sinif nedir?

Sinif(class) - Python “obyekt yönümlü proqramlaşdırma dilidir”. Bu o deməkdir ki, demək olar ki, bütün kodlar siniflər adlanan xüsusi konstruksiyadan istifadə etməklə həyata keçirilir. Sinif obyektlərin yaradılması üçün kod şablonudur. Obyektlərin üzv dəyişənləri və onlarla əlaqəli davranışları var. Pythonda sinif açar sözlə yaradılır class.

Obyekt nedir?
obyekt - obyektlər classlardan yaranır. 

Atribut ve metod arasindaki ferqi izah edin.

    Atribut == xüsusiyyətlər, Metod == əməliyyatlar/ hərəkətlər deməkdir.

    atribut: Nöqtəli ifadələrdən istifadə edərək adla istinad edilən obyektlə əlaqəli dəyər. Məsələn, əgər o(self) obyekti a atributuna malikdirsə, ona o.a kimi istinad ediləcək

    metod: Sinif orqanında müəyyən edilmiş funksiya. Əgər həmin sinfin nümunəsinin atributu kimi çağırılarsa, metod misal obyektini ilk arqumenti kimi alacaq (bu adətən öz adlanır). Funksiyaya və daxili əhatə dairəsinə baxın.
Məsələn:
class C:

    c = 20                      # class attribute

    def __init__(self, d):      # "dunder" method
        self.d = d              # instance attribute