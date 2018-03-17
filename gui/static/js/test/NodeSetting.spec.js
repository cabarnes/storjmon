import { shallow } from '@vue/test-utils';
import NodeSetting from '../components/NodeSetting.vue';

describe('NodeSetting.vue', () => {
  it('hides error message when not set', () => {
    const wrapper = shallow(NodeSetting);

    const span = wrapper.find('span');
    expect(span.exists()).toBe(false);
  });

  it('shows error message when set', () => {
    const wrapper = shallow(NodeSetting);
    wrapper.setData({
      errorMessage: 'test message',
    });

    const span = wrapper.find('span');
    expect(span.exists()).toBe(true);
    expect(span.text()).toBe('test message');
  });

  it('sends event when button clicked', () => {
    const wrapper = shallow(NodeSetting);

    wrapper.find('button').trigger('click');
    expect(wrapper.emitted('get-info').length).toBe(1);
  });
});
