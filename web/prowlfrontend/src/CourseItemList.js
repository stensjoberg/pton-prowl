import React, { Component } from 'react'
import Radium from 'radium'
import CourseItem from './CourseItem'
import { Link, Route } from 'react-router-dom'
import { styles } from './styles'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class CourseItemList extends Component {
  state = {
    courses: [],
  }

  async componentDidMount() {
    try {
      const res = await fetch('http://0.0.0.0:8000/api/v1/courses/')
      const courses = await res.json()
      this.setState({
        courses
      })
      console.log("Courses:")
      console.log(courses)
      console.log("State:")
      console.log(this.state)
    } catch (e) {
      console.log(e)
    }
  }

  render() {
    return (
      <div className="flexcontainer vert">
      {this.state.courses.map((item, i) => (
        <Link to={'/course/'+item.id}>
          <CourseItem
            key={item.id}
            id={item.id}
            url={item.url}
            title={item.title}
            i={i}
          />
        </Link>
      ))}
      </div>
    )
  }
}

export default Radium(CourseItemList)
