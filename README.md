# kalliope-writer

A neuron to write text in active window for linux


## Synopsis

Make kalliope write you text from speech

## Installation

  ```
  kalliope install --git-url https://github.com/SpawNBK/writerneuron_kalliope
  ```


## Options

| parameter  | required | default   | choices  | comment                                                                                    |
|------------|----------|-----------|----------|--------------------------------------------------------------------------------------------|
| *          | Yes      |           | String* * | Your incoming query                                                                        |



## Return Values

| Name                | Description                                                                           | Type     | sample   |
| ------------------- | ------------------------------------------------------------------------------------- | -------- | -------- |
| *                   | The query you sent                                                                    | String   |          |

As describe above, return values are all the input values.


## Synapses example

Play a playlist by giving its name to kalliope

```yaml
  - name: "Write"
    signals:
      - order: "write text{{ query }}"
    neurons:
      - writer:
          query: "{{query}}"
```

