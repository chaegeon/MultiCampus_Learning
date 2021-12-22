// 자바스크립트의 한 줄 주석
/*
멀티라인 주석
여러줄에 대해 주석으로 처리할 수 있다
*/ 

// 변수의 정의와 선언이 따로 있다. 파이썬은 선언은 없었음.

console.log('--변수의 선언--');
// 변수의 선언
var var1; // 보통 var 키워드는 사용하지 않는 것이 좋다
let var2; // 보통 이런 방식으로 사용함

var a = 5;
let b = '하이';

function add(a, b){
    return a + b;
} 


let var3 = 5; // 나눠서 쓴 것.

console.log('--변수의 정의--');
// 변수의 정의
var2 = 10; 
console.log(var2);

console.log(add(5, 10));

// 새로운 변수는 선언을 먼저 해주든, 선언과 정의를 동시에 하든
// 둘 중 하나를 해줘야 한다.

console.log('--자료의 타입--');
// 자료의 타입
console.log(typeof 10);
console.log(typeof 10.0);
console.log(typeof 'hello'); // 문자열 타입
console.log( typeof true);

// 파이썬에서 없는 타입
console.log(typeof null);
console.log(typeof undefined);
console.log(typeof NaN); // Not a Number
console.log(typeof Infinity );

console.log('--연산자--');
// 연산자
// 몫 연산은 없다
console.log( 2 + 3);
console.log( 2 - 3);
console.log( 2 * 3 );
console.log( 2 / 3 );
console.log( 2 % 3 );
console.log( 2 ** 3 );

//몫을 구하려면
let q;
q = 3 / 2;
q = parseInt(q)
console.log(q);

console.log('--파이썬에서는 없는 연산자--');
//피이썬에서는 없는 연산자
//증감연산자
// 1씩증가하거나 1씩 감소할 수 있다
let number = 2; // 메모리에 키워드를 추가할 떄에는 키워드로 정의
console.log( ++number);
console.log( --number);

//앞에 붙으면 전위식, 뒤에 붙으면 후위식. 전위식과 후위식은 차이가 있다

// 전위식은 증가만저하고 나머지 명령을 핼
number = 2; // 변수를 재지정하는 거라 키워드를 안 붙여도 됨
console.log( number++ ); // number +=1
// 실제로는 1증가했다
// 후위식은 명령을 먼저 처리하고 나중에 1을 증감
console.log( number );

console.log('--비교 연산자--');
// 비교연산자
// 자바스크립트는 비교할 때 타입을 고려하지 않음
console.log( 1 == '1' ); // 파이썬에서는 펄스인데 자바스크립트는 트루
// 숫자1과 문자1은 동일하다고 봄

// 자바스크립트에서 타입까지 함께 고려해서 비교하는 방법
console.log(1 === '1');

console.log('--논리연산자--');
// 논리연산자
// dAND, OR, NOT
// 자바스크립트는 &&, ||, ! 기호로 사용
console.log( true && false);
console.log( true || false);
console.log( ! true);


console.log('--자바스크립트의 If문-- ');
// If 의 형태
/*

if (명제) {

} else if(명제) {

} else {

}

자바스크립트는 블록의 시작' { '과 끝' } '을 중괄호로 감싸서 표현

*/

// 윤년구하기
let year = 2000;
if ( ( year % 4 == 0)  &&  (year % 100 != 0 ) || ( year % 400 == 0 )) {
    console.log('윤년입니다')
} else {
    console.log('평년입니다')
}
// 추가적으로 witch-case 문이 있음
// 현대 프로그래밍에서는 거의 안쓰는 추세이기도 하고, 혼란만 가중될 것 같아서 패스


// 배열과 반복
console.log('--배열--');
//배열
// 자바스크립트는 배열이라는 타입이 존재( 파이썬의 리스트와 동일 )

//배열을 생성하는 방법은 3가지가 있다
let array = []; // 빈 배열 객체 생성
// let array = Array(10, 20, 30, 40);   => Array 클래스의 생성자를 이용해서 객체 생성
// let array = newq Array(); => new연산자를 이용한 Array 객체 생성

array = [10, 20, 30, 40];
console.log( array );
console.log( array[0] ); // 인덱스가 0부터 출발하는 것도 동일
// 다만 음수 인덱스는 없다.
// 슬라이스도 없다.
console.log( array[0], array[2]);


// 파이썬의 append 와 같은 역할을 하는 것이 push
// 배열에 50을 추가해보자
array.push(50);
console.log( array );
// 인덱스 범위를 넘어가는 경우
console.log( array[10] ); // 에러가 났다기 보다는 정의가 되지 않았다고 알려줌

// 자바스크릡트는 배여르이 원소를 이렇게도 추가할 수 있다
array[10] = 100;
console.log( array); // 인덱스가 없으면 만들어버림...
//대신 0,1,2,3,4,10 인덱스에만 값이 있으므로 5, 6, 7, 8, 9 인덱스는 undefined로 나옴

// 자바스크립트는 배열을 파이썬의 dict처럼 사용할 수 있다
// 연관배열 이라고 함
let arr = [];
arr['first'] = 10; // 이렇게만 해도
console.log(arr); // 딕셔너리 [Key:Value] 구조가 됨

console.log('--반복문--');
// for, while, for each
//파이썬의 for 와는 완전히 다름
//while의 또다른 표현정도로 이해

//1부터 10까지의 반복을 while로 짠다면
let i = 1; // 초기값
while( i <= 10 ) { // 조건
    console.log(i);
    i++;            // 증감
}

/*
while( i <= 10) 뒤에 ;를 적었더니 그 뒤로 계속 실행이 안 됐었음
터미널에 커서가 가 있었는데, 
이건 무한루프에 빠지는 등의 경우에 아직 작업이 안 끝났다는 의미
그래서 Ctrl + C 로 빠져나왔음
그랬더니 막혀서 실행되지 않았던 작업들이 쭈루룩 나옴
*/



//자바스크립트의 for는 초기값; 조건; 증감; 한줄에 표현
//for( 초기값; 조건; 증감;)
//표현만 다르고, 동작은 while과 동일
for( let i =1; i <= 10; i++) {
    console.log(i);
}

// for loof 와 동일한 동작을 하는 for each
console.log(array);
for (let x of array ) {
    console.log ( x );
}

// 1부터 n까지의 총합 구하기
let n = 20;
let total = 0;
for( let i =0; i <= n; i++) {
    total += i;
}
console.log(total);

// 자바스크립트의 클래스는 파이썬보다 더 지랄맞음
console.log('--함수--');
// 함수
// 자바스크릡트의 함수도 파이썬과 비슷. 기능은 동일함
// 자바스크립트는 'function' 키워드로 함수를 정의한다

function func(a, b) { // 매개변수 가질 수도 있고 안 가질 수도 있고
    return a + b; //리턴문장 가질 수도있고 안 가질 수도 있고
}
// 역시 함수를 호출해야 실행. 지역변수/전역변수 개념도 동일
console.log( func( 10, 20) );

//가변인자는 파이썬과 좀 다름
function add() {
    //파라미터는 지정하지 않고, 가변인자 객체가 따로 존재한다
    console.log( arguments ); // arguments 라는
}
add(1,2,3,4,5,6,7, );

function add() {
    let sum = 0;
    for(let i=0; i< arguments.length; i++){
        sum += arguments[i];
    }
    return sum;
}
ret = add( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
console.log( ret );

console.log('--지역변수와 전역변수--');
//지역변수, 전역변수. 파이썬과 동일
let mem = 10;
function func1() {
    let mem = 20;
}
func1();
console.log(mem);

console.log('--디폴트 파라미터--');
function func2(a,b) {
    console.log( a, b );
}
func2(); // 에러 안 남
// 파라미터 지정
function func3(a,b = 2 ) {
    console.log( a, b );
} 
func3();


console.log('--자바스크립트의 클래스--');
class Person{
    // 클래스 변수가 아님
    // 필드 선언(public과 private 선언)
    // 속성 앞에 '#'을 붙이면 privat 으로 설정할 수 있다
    #name; // privat 선언
    #age;

//파이썬의 클래스 변수와 같은 기능
static nation='Korea'; // static을 붙여줌

    // 생성자
    constructor(name, age) {
        // this는 파이썬의 self와 같은 역할
        // 따로 파라미터로 정의하지 않아도 항상 정의되어 있다.
        this.#name = name;
        this.#age = age;
    };
    //정적메소드
    static staticMethod(){
        console.log( Person.nation );
    }

    // getter 과 setter
    get name() {
        return this.#name;
    }

    set name(name){
        this.#name = name;
    }

    //class 내에서 메소드를 정의할 떄는 'function' 키워드는 생략
    info() {
        console.log(this.#name, this.#age);
    }
}

//객체생성
object = new Person('장동건', 22);
object.info();

//은닉성
//외부에서는 접근 불가능
//object.#name='원빈';
//object.info();

//정적변수는 클래스 이름을 접근 가능
console.log( Person.nation );
Person.staticMethod();


console.log('--getter와 setter--');
// getter과 setter를 사용하는 방법은 파이썬과 동일하다
object.name = '원빈';
console.log( object.name );
object.info();

