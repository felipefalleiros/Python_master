from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    # o metodo deve começar com o sufixo clean_ e dizer o campo a ser validado
    def clean_value(self):
        # adicionar type hint dizendo que value pode ser float ou None
        value: float | None = self.cleaned_data.get('value')
        if not value or value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000,00')
        return value
        
    def clean_factory_year(self):
        factory_year: int | None = self.cleaned_data.get('factory_year')
        if not factory_year or factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastrar fabricados antes de 1975')
        return factory_year