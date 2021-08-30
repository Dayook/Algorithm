// 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다. 이 공가은 1 x 1 크기의 정사각형으로 나누어져 있다.
// 가장 왼쪽 위 좌표는 (1,1)이며 가장 오른쪽 아래 좌표는 (N,N)에 속한다.
// 여행가 A는 ㅏㅇ 하 좌 우 방향으로 이동할 수 있으며 시작 좌표는 항상 (1,1)dlek.
// 우리앞에는 여행가가 이동할 계획이 적힌 계획서가 놓여 있다.
// 이 때, A가 N x N 크기의 정사각형을 벗어나는 움직임은 무시된다.

let space = 5;
let plans = ["R", "R", "R", "U", "D", "D"];

let move_types = ["U", "D", "L", "R"];
let dx = [0, 0, -1, 1];
let dy = [1, -1, 0, 0];
let location_x = 1;
let location_y = 1;

function move_plan(space, plans) {
  for (var plan in plans) {
    let i = 0;
    while (i < move_types.length) {
      if (move_types[count] === plan) {
        var nx = x + dx[count];
        var ny = y + dy[count];
        break;
      }
      i += 1;
    }
    if ( nx < 1 || ny < 1 || nx > n || ny > n )
     {
      continue;
    }
    location_x = nx;
    location_y = ny;
  }

  return [location_x, location_y];
}
console.log("지도 문제");
console.log(move_plan(5, ["R", "R", "R", "U", "D", "D"]));
