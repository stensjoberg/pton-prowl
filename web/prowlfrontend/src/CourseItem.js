import React, { Component } from 'react'
import { Link, Route } from 'react-router-dom'
import Radium from 'radium'
import { styles } from './styles'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class CourseItem extends Component {
  handleAddition = async (event) => {
    event.preventDefault()
    console.log(this.props.id)
    try {
      const res = await fetch('http://0.0.0.0:8000/api/v1/courses/', {
        method: 'POST',
        headers: {
          'Authorization': 'Token ' + localStorage.getItem('token'),
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          id: this.props.id,
        })
      })
      console.log(res)
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div className="flexcontainer hor coursebox" style={Object.assign({},
        this.props.i % 2 && styles.tigerStripe
      )}>
        <p>
          {this.props.title}
        </p>
        <button onClick={this.handleAddition}>+</button>
      </div>
    );
  }
}

export default Radium(CourseItem)
