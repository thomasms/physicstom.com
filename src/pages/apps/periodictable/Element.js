import React from 'react';

function GridColourElement(props){

  const style = {
      gridColumn: props.gridPosition,
      gridColumnEnd: props.gridPosition,
      borderColor: props.colour
  };

  return(
    <div className="apps-periodictable-element"
          style={style}
          onMouseEnter={(element) => props.handleOnMouseEnter(props.element)}
          onMouseLeave={(element) => props.handleOnMouseLeave(props.element)}
          onClick={(element) => props.handleOnClick(props.element)}>
      <div className="apps-periodictable-element-atomic">
        {props.element.atomic}
      </div>
      <div className="apps-periodictable-element-symbol">
        {props.element.symbol}
      </div>
    </div>
  );
}

export { GridColourElement };
