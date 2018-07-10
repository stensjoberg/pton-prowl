import React, { Component } from 'react'
import Radium from 'radium'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';


class LogoutForm extends Component {

  handleLogout = async (event) => {
    localStorage.removeItem('token')
    this.props.history.push('/login')
  }

  render() {
    return (
      <button onClick={this.handleLogout}>
        Logout
      </button>
    );
  }
}

export default Radium(LogoutForm)
