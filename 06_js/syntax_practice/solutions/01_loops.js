/*
  [while문 연습]
  아래의 조건을 만족하는 while문을 작성하세요.
  - 주어진 변수 evenNumber를 2씩 증가시키고, 해당 값을 출력합니다.
  - evenNumber가 6이 되면 반복문을 종료합니다.
*/

let evenNumber = 0

while (evenNumber < 6) {
  console.log(evenNumber) // 0, 2, 4
  evenNumber += 2
}

/*
  [for문 연습]
  아래의 조건을 만족하는 for문을 작성하세요.
  - oddNumber라는 이름의 변수를 선언 및 1로 초기화합니다.
  - 매 시행마다 oddNumber를 2씩 증가시키고, 해당 값을 출력합니다.
  - oddNumber가 5가 되면 반복문을 종료합니다.
*/

for (let oddNumber = 1; oddNumber < 5; oddNumber += 2) {
  console.log(oddNumber) // 1, 3
}

/*
  [for... in 연습]
  - 주어진 객체를 순회하면서 예시와 같이 출력합니다.
  - 예시) title: '벤자민 버튼의 시간은 거꾸로 간다'
*/

const bestMovie = {
  title: '벤자민 버튼의 시간은 거꾸로 간다',
  releaseYear: 2008,
  actors: ['브래드 피트', '케이트 블란쳇'],
  genres: ['romance', 'fantasy']
}

for (const key in bestMovie) {
  console.log(`${key}: ${bestMovie[key]}`)
}

/*
  [for... of 연습]
  - 주어진 배열을 순회하면서 예시와 같이 출력합니다.
  - 예시) title: '어바웃 타임'
*/

const movies = [
  { title: '어바웃 타임' },
  { title: '굿 윌 헌팅' },
  { title: '인턴' }
]

for (const movie of movies) {
  console.log(`title: ${movie.title}`)
}
