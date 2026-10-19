from pyscript import display, document


def member_submission(e):
    document.getElementById('result').innerHTML = " "

    first_name = document.getElementById('firstname').value.capitalize().strip()
    last_name = document.getElementById('surname').value.capitalize().strip()
    member_name = {first_name + " " + last_name}

    g7_members = {'Lusviminda Diaz', 'Consuelo Baja', 'Romero Imperial', 'Ernesto Salazar'}
    g8_members = {'Ferdie Delos Santos', 'Rogelio Felicided', 'Ricardo Batumbakal', 'Conching Rosales'}
    g9_members = {'Russel Bautista', 'Hilario Quintero', 'Travis Rapid', 'Juanito Macalintal'}
    g10_members = {'Ester Vinluan', 'Ramon Lucas Ponce', 'Enrique Manalo', 'Joseph Ernesto Pangilinan'}

    total_members = g7_members | g8_members | g9_members | g10_members | member_name

    display(f'The members are: {total_members}', target='result')
    display(f'Total number: {len(total_members)}', target='result')
