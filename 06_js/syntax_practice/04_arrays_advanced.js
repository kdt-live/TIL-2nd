/*
 [배열 관련 주요 메서드 연습 심화 1 - map]

 속력값(distance/time)을 저장하는 배열 speeds를 만드세요.
*/

const trips = [
  { distance: 34, time: 10 },
  { distance: 90, time: 50 },
  { distance: 59, time: 25 }
]

/*
 [배열 관련 주요 메서드 연습 심화 2 - filter]

 주어진 배열의 요소 중 특정 문자(query)가 포함되는 요소만 모아서 새로운 배열을 반환하세요.
*/

const languages = ['python', 'javascript', 'html', 'java']
const query = 'java'

/*
 [배열 관련 주요 메서드 연습 심화 3 - forEach, reduce]

 주어진 배열을 사용하여 다음과 같은 객체를 만드세요.
 {
   smith: 90,
   peter: 80,
   anna: 85,
 }
*/

const scores = [
  { name: 'smith', score: 90 },
  { name: 'peter', score: 80 },
  { name: 'anna', score: 85 }
]

/*
 [배열 관련 주요 메서드 연습 심화 4 - find]

 주어진 accounts 배열에서 balance가 24,000인 사람을 찾으세요.
*/

const accounts = [
  { name: 'sophia', balance: 1200 },
  { name: 'john', balance: 50000 },
  { name: 'tailer', balance: 24000 }
]

/*
 [배열 관련 주요 메서드 연습 심화 5 - some]

 주어진 requests 배열에서 status가 pending인 요청이 있는지 확인하세요.
*/

const requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' }
]

/*
 [배열 관련 주요 메서드 연습 심화 6 - every]

 주어진 users 배열을 통해 모든 유저의 상태가 submmited인지 여부를 확인하세요.
*/

const users = [
  { name: 'sophia', submitted: true },
  { name: 'john', submitted: true },
  { name: 'tailer', submitted: false }
]
