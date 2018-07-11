export async function getCourse(id) {
  try {
    const response = await fetch('http://0.0.0.0:8000/api/v1/courses/' + id, {
          headers: {
          'Authorization': 'Token ' + localStorage.getItem('token'),
        }
      }
    )
    const course = await response.json()
    return course
  } catch (e) {
    console.log(e)
  }
}

export async function getUser(netid) {

    try {
      const response = await fetch('http://0.0.0.0:8000/api/v1/users/' + netid, {
          headers: {
            'Authorization': 'Token ' + localStorage.getItem('token'),
          }
      })
      const user = await response.json()
      return user
    } catch (e) {
      console.log(e)
    }

}
