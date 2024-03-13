function InverteString(s) {
  let nova_string = '';
  for (let i = s.length - 1; i >= 0; i--) {
    nova_string += s[i];
  }
  return nova_string;
}

let string = 'Estágio em desenvolvimento na Target Sistemas';

console.log(InverteString(string));
