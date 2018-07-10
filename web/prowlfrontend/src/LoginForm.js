import React, { Component } from 'react'
import Radium from 'radium'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';


class LoginForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      netid: '',
      password: ''
    };
    this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleLogin = async (event) => {
    event.preventDefault()
    try {
      const res = await fetch('http://0.0.0.0:8000/api/v1/rest-auth/login/', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: this.state.netid,
          password: this.state.password
        })
      })
      const payload = await res.json()
      localStorage.setItem('token', payload['key'])
      this.props.history.push('/')
    } catch (e) {
      console.log(e)
    }
  }

  render() {
    return (
      <form onSubmit={this.handleLogin}>
        <label htmlFor="netid"><b>NetID</b></label>
        <input type="text" onChange={this.handleInputChange} placeholder="Enter NetID" name="netid" required />

        <label htmlFor="password"><b>Password</b></label>
        <input type="password" onChange={this.handleInputChange} placeholder="Enter Password" name="password" required />

        <input type="submit" value="Login" />
      </form>
    );
  }
}

export default Radium(LoginForm)
