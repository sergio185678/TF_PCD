window.addEventListener('DOMContentLoaded', () => {
  fetch('/api/message')
    .then(response => response.json())
    .then(data => {
      const movementsContainer = document.getElementById('movements-container');
      data.messages.forEach(message => {
        const movementCard = createMovementCard(message);
        movementsContainer.appendChild(movementCard);
      });
    })
    .catch(error => {
      console.error('Error fetching movements:', error);
    });
});

function createMovementCard(message) {
  const { cmd, hostname, player } = message;
  const { team, home, from } = player;

  const movementCard = document.createElement('div');
  movementCard.className = 'movement-card';

  const cmdElement = document.createElement('p');
  cmdElement.textContent = `Comando: ${cmd}`;
  movementCard.appendChild(cmdElement);

  const hostnameElement = document.createElement('p');
  hostnameElement.textContent = `Hostname: ${hostname}`;
  movementCard.appendChild(hostnameElement);

  const teamElement = document.createElement('p');
  teamElement.textContent = `Equipo: ${team}`;
  movementCard.appendChild(teamElement);

  const homeElement = document.createElement('p');
  homeElement.textContent = `Home: ${home}`;
  movementCard.appendChild(homeElement);

  const fromElement = document.createElement('p');
  fromElement.textContent = `Desde: ${from}`;
  movementCard.appendChild(fromElement);

  return movementCard;
}
