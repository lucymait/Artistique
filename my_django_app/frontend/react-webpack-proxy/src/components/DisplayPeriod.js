import React, { useState, useEffect } from 'react'
import 'bulma'

const DisplayPeriod = () => {
  const [data, setData] = useState([])

  useEffect(() => {
    fetch('/api/artwork/period')
      .then(resp => resp.json())
      .then(resp => setData(resp))
  })

  return <div>
    {data.map((period, key) =>
      // need a key
      <div className="period" key={key}>
        {period.name}
      </div>
    )}
  </div>
}

export default DisplayPeriod