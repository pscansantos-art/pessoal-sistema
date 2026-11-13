from django.shortcuts import render

def index(request):
    context = {
        # Dados do Mini Currículo
        'nome': 'Bruno de Jesus Santos',
        'idade': 20,
        'cargo': 'Jovem Aprendiz Administrativo no Grupo André Guimarães',
        'resumo': 'Estudante de tecnologia focado em desenvolvimento de software e rotinas administrativas/financeiras, com experiência prática em sistemas corporativos como TOTVS RM e Fluig.',
        'formacao': [
            'Bacharelado em Ciência da Computação - IFBA Camaçari (3º Semestre)',
            'Técnico em Desenvolvimento de Sistemas - SENAI Lauro de Freitas (4º Semestre)',
            'Técnico em Informática - IF Baiano (4º Semestre)'
        ],
        'habilidades': [
            'Python (Django)', 'Java', 'C', 'HTML & CSS', 'JavaScript',
            'MySQL Workbench', 'Docker', 'Git & GitHub', 'TOTVS RM', 'Fluig'
        ],

        # Dados do Filme Favorito (abre ao clicar)
        'filme': {
            'titulo': 'Interestelar',
            'ano': '2014',
            'genero': 'Ficção Científica / Drama',
            'diretor': 'Christopher Nolan',
            'sinopse': (
                'Em um futuro próximo onde a Terra enfrenta uma crise ambiental severa, '
                'um grupo de exploradores lidera uma missão através de um buraco de minhoca '
                'no espaço para encontrar um novo planeta habitável e garantir a sobrevivência da humanidade.'
            ),
            'motivo': 'Destaca-se pela trilha sonora impecável de Hans Zimmer, precisão científica e pela carga emocional da relação entre pai e filha.'
        },

        # Dados da Banda Favorita (abre ao clicar)
        'banda': {
            'nome': 'Red Hot Chili Peppers',
            'genero': 'Rock Alternativo / Funk Rock',
            'origem': 'Los Angeles, Califórnia (1983)',
            'descricao': (
                'Uma das bandas mais icônicas do rock mundial, conhecida por misturar '
                'linhas de baixo marcantes no estilo funk com riffs melódicos e energia intensa no palco.'
            ),
            'musicas_destaque': [
                'Californication',
                'By the way',
                'Otherside',
                'Under the Bridge'
            ]
        }
    }
    return render(request, 'favoritos/index.html', context)