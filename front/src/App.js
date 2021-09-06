import React, {useState,useEffect} from 'react';

function App() {
	const [users, setUsers] = useState([]);
	useEffect(()=>{
		fetch('/tests')
		.then(res => res.json())
		.then(data => {
			console.log(data)
            setUsers(data)
		})
    },[]);
  return (
    <>
	  <h1>안녕하세요</h1>
	  <ul>{users.map((user, index)=><li key={index}>{user.name}, {user.nidk}</li>)}</ul>
    </>
  );
}

export default App;