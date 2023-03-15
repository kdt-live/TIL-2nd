/*
  [Object 요소 접근 연습]

  주어진 객체에서 items의 첫번째 아이템의 name을 result 변수에 할당하세요.
*/

const data = {
  id: 42,
  items: [
    {
      id: 1,
      name: 'foo'
    },
    {
      id: 2,
      name: 'bar'
    }
  ]
}

const result = data.items[0].name
console.log(result) // 'foo'

/*
[Object 축약 문법]

아래 변수들을 속성으로 가지는 Object를 축약문법을 활용하여 작성하세요.
*/

const username = 'hailey'
const contact = '010-1234-5678'

// ES5
const user1 = {
  username,
  contact
}

// ES6+
const user2 = {
  username,
  contact
}

console.log(user1)
console.log(user2)
